# Running

## Windows

```powershell
$env:FOO="zap"; python .\main.py ; write-host "foo = $env:FOO" -ForegroundColor Red
```


## Linux

```bash
FOO=bar python main.py ; echo $FOO

# 

FOO=zap && python main.py && printf "\e[31;1mfoo = $FOO\n"


```