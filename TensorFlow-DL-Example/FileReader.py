# Test file to read the CIFAR dataset

def unpickle(file):
    """
    Unpickle the dataset from disk
    :param file:
    :return a dict with the dataset:
    """
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo)
    return dict


# Read the file in a dict
dict = unpickle('/Users/sebas/PycharmProjects/tensorflow-DL-example/TensorFlow-DL-Example/files/cifar-10-batches-py/data_batch_1')

# Analyze the dict
# Print the dict
print dict
# Print the type of dict
print type(dict)
# Print the methods and attributes of the dict. This is useful for knowing what we can do
print dir(dict)
# The keys() function in any dictionary shows the keys
print dict.keys()
# Keys: data, labels, batch_label, filenames
# how big is the dict?
# print the amount of 'rows'
print len(dict['data'])
# print the amount of 'columns' in row 0
print len(dict['data'][0])

