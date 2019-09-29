from pset_1.hash_str import get_csci_salt, get_user_id, hash_str


def get_user_hash(username, salt=None):
    salt = salt or get_csci_salt()
    return hash_str(username, salt=salt)


if __name__ == "__main__":

    for user in ["gorlins", "frankiekienlam"]:
        print("Id for {}: {}".format(user, get_user_id(user)))

    data_source = "data/hashed.xlsx"

    # TODO: read in, save as new parquet file, read back just id column, print

# Parquet Question

from pset_1.io import atomic_write

import pandas as pd

import pyarrow as pr

# transform excel file into .parquet file with the same content
df = pd.read_excel(data_source,index_col=0)
df.to_parquet('hashed.parquet','pyarrow')

# Print out the list of hashed_id using atomic_write
hash_id_list = list(pr.parquet.read_table('hashed.parquet', columns=['hashed_id']))
hash_id_list_str = str(hash_id_list)

with atomic_write("hashed_id_list.txt") as f:
    f.write(hash_id_list_str)

with open ("hashed_id_list.txt") as f:
    lines = f.read()
    print(lines)

