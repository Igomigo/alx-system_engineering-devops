# Using Puppet, create a manifest that kills a process named killmenow

exec { 'kill command':
    path    => '/bin/',
    command => 'pkill killmenow',
}
