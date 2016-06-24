__author__ = 'johnfulgoni'

# import api_attempt
import create_dataset
import network_graph

jack_filename = 'Data/Jacks_Facebook.csv'

def main():
    # api_attempt.start()

    name_list = []
    raw_dataset = []
    key_list = {}

    jack_raw_data = create_dataset.import_raw_file(jack_filename)
    raw_dataset.append(jack_raw_data)
    name_list.append('Jack Holtgreive')

    for dataset, name in zip(raw_dataset,name_list):
        key_list = create_dataset.anonymize_data(key_list, dataset, name)

    print key_list['John Fulgoni']

    G = network_graph.create_graph(raw_dataset,name_list,key_list)
    #network_graph.print_edges(G)
    network_graph.mat_draw(G)

def print_friends(data, name):
    print "Number of Friends for " + name + ": " + str(len(data))
    for friend in data:
        print friend

if __name__ == '__main__':
    main()