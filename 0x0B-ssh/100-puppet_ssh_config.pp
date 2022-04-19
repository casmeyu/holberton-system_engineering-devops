exec { 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => '/usr/local/bin/:/bin/',
}

# Dont know why sed doesnt change the file

# exec { '/etc/ssh/ssh_config':
#  command => 'sed -i "s/.*PasswordAuthentication.*/PasswordAuthentication no/g" /etc/ssh/sshd_config',
#  path    => '/usr/local/bin/:/bin/',
# }
