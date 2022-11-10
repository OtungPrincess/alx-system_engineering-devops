# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec {'hard':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 65536/g' /etc/security/limits.conf; /sbin/sysctl -p",
provider => 'shell',
}
# Increase soft file limit for Holberton user.
exec {'soft':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => "sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 65536/g' /etc/security/limits.conf; /sbin/sysctl -p",
provider => 'shell',
}
