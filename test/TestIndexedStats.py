from simkit.stats import IndexedSimpleStatsTally
from simkit.simkit import IndexedStateChangeEvent
from simkit.simkit import SimEntityBase
from simkit.rand import RandomVariate

source = SimEntityBase()
print(source.describe())

name = 'foo'
rv = RandomVariate.getInstance('Exponential', mean=2.3)

stats = IndexedSimpleStatsTally(name)
for i in range(1000):
    for j in range(4):
        event = IndexedStateChangeEvent(j, source, name, rv.generate())
        stats.stateChange(event)

print(stats)
