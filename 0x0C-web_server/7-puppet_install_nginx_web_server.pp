# Puppet file for configuring a web server with nginx

package { 'nginx':
  ensure => 'latest',
}

#config
file_line { 'nginx config':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n\terror_page 404 /custom-404.html\n',
}

# html files
file { '/var/www/html//index.nginx-debian.html':
  ensure  => 'file',
  content => 'Hello World',
}
file { '/var/www/html/custom-404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page",
}

#run nginx server
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

