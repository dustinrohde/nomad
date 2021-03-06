from nomad.entity import Entity, Stats
from nomad.roles import *
from nomad.entities import *


class Nomad(Entity):
    '''The player-controlled entity.'''

    object_factory = {
        frozenset(('sharp rock', 'stick')): (3, spear),
        }

    def __init__(self, los, stats=Stats(3, 3, 3)):
        '''Initialize the nomad.

        :Parameters:
            `los` : int
                How far the nomad sees in any direction. Should be
                equal to the plains' radius, once set.
        '''
        super().__init__('nomad', False, stats, roles=dict(
                         mortal=Mortal(),
                         tactile=Tactile(self.object_factory)))
        self.los = los

    def move(self, dx, dy):
        '''Move the nomad, shifting the plains with it to simulate
        line of sight.
        '''
        if not self.plains.walkable_at(self.x + dx, self.y + dy):
            return
        self.plains.shift(-dx, -dy)
        self.plains.move_entity(self, self.x + dx, self.y + dy)
