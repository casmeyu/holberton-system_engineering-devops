# Executes a pkill command
exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => '/usr/local/bin:/bin/',
}
