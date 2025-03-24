if you want to run email server localy without having smtp setting in .env
aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025


change envs_template directory to envs and change template.env to .env
