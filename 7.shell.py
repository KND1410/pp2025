import os

while True:
    cmd = input("> ")

    if cmd == "exit":
        break
    
    output_file = None
    input_file = None
    pipe_cmd = None

    if ">" in cmd:
        parts = cmd.split(">")
        cmd = parts[0].strip()
        output_file = parts[1].strip()
    
    if "<" in cmd:
        parts = cmd.split("<")
        cmd = parts[0].strip()
        input_file = parts[1].strip()

    if "|" in cmd:
        parts = cmd.split("|")
        cmd = parts[0].strip()
        pipe_cmd = parts[1].strip()
    
    args = cmd.split()
        
    if not args:
        continue


    if pipe_cmd:
        r, w= os.pipe()

        pid1 = os.fork()
        if pid1 == 0:
            os.close(r)
            os.dup2(w, 1)
            os.close(w)
            os.execlp(args[0], *args)
        
        pid2 = os.fork()
        if pid2 == 0:
            os.close(w)
            os.dup2(r, 0)
            os.close(r)
            pipe_args = pipe_cmd.split()
            os.execlp(pipe_args[0], *pipe_args)
        
        os.close(w)
        os.close(r)
        os.wait()
        os.wait()
    
    else:
        pid = os.fork()

        if pid == 0:
            if output_file:
                fd = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
                os.dup2(fd, 1)
                os.close(fd)

            if input_file:
                fd = os.open(input_file, os.O_RDONLY)
                os.dup2(fd, 0)
                os.close(fd)

            os.execlp(args[0], *args)
        else:
            os.wait()
