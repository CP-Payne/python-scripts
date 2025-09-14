import paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

try:
    client.connect("bandit.labs.overthewire.org", 2220, "bandit0", "bandit0")
    stdin, stdout, stderr = client.exec_command("cat readme")
    print("STDOUT:")
    print(stdout.read().decode())
    print("STDERR:")
    print(stderr.read().decode())

except paramiko.AuthenticationException:
    print("Authentication failed.")
except paramiko.SSHException as e:
    print(f"SSH error: {e}")
finally:
    client.close()

# regex for pass: \b[A-Za-z0-9]32\b
