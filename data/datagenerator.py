# %%
import pandas as pd
import numpy as np
import random
import string


class DataGen:
    def __init__(self):
        pass

    # Function to generate a random unique alphanumeric customer ID
    def generate_customer_id(self, length=8):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def generate_ecomm_data(self, num_records=1000):
        data = {
            "Unique Customer ID": [
                self.generate_customer_id() for _ in range(num_records)
            ],
            "Age": np.random.randint(18, 80, num_records),  # Age between 18 and 80
            "Gender": np.random.choice(["Male", "Female"], num_records),
            "Income": np.random.choice(["<15k", "15k-75k", ">75k"], num_records),
            "Prior Visits": np.random.randint(1, 20, num_records),
            "Customer Type": np.random.choice(["New", "Existing"], num_records),
            "Order Value": np.round(np.random.uniform(10.00, 10000.99, num_records), 2),
            "Read Reviews": np.random.randint(0, 1, num_records),
            "Purchase made": np.random.choice([0, 1], num_records),
        }

        return pd.DataFrame(data)


if __name__ == "__main__":
    datagen = DataGen()
    dataset = datagen.generate_ecomm_data()
    print(dataset.head())
