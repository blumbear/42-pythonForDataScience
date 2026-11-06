from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


for elem in ft_tqdm(range(333)):
    sleep(0.01)
print()
print(ft_tqdm.__doc__)

for elem in tqdm(range(333)):
    sleep(0.01)
print()
print(tqdm.__doc__)
