from mininet.topo import Topo

class RingTopology( Topo ):
    def build( self ):
        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's1' )
        middleSwitch_1 = self.addSwitch( 's2' )
        middleSwitch_2 = self.addSwitch( 's3' )
        middleSwitch_3 = self.addSwitch( 's4' )
        rightSwitch = self.addSwitch( 's5' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, middleSwitch_1 )
        self.addLink( middleSwitch_1, middleSwitch_2 )
        self.addLink( middleSwitch_2, middleSwitch_3 )
        self.addLink( middleSwitch_3, rightSwitch )
        self.addLink( rightSwitch, leftSwitch )
        self.addLink( rightSwitch, rightHost )


topos = { 'ringtopo': ( lambda: RingTopology() ) }

