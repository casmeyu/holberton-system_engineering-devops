file_line { '/etc/ssh/ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication	no'
  match  => '\s*PasswordAuthentication\s*\w*',
}

file_line { '/etc/ssh/ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => 'IdentityFile ~/.ssh/id_rsa',
}
