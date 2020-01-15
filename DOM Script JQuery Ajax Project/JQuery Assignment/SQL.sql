Select f.ID
from EmplJan j 
join EmplFeb f
on j.ID = f.ID
Where j.RegionCode <> f.RegionCode