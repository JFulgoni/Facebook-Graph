__author__ = 'johnfulgoni'

# import api_attempt
import create_dataset
import network_graph

jack_filename = 'Data/Jacks_Facebook.csv'

def main():
    # api_attempt.start()

    name_list = []
    dataset = []

    jack_data = create_dataset.process_file(jack_filename)
    dataset.append(jack_data)
    name_list.append('Jack Holtgreive')

    G = network_graph.create_graph(dataset,name_list)

    print G.edges()
    print_friends(dataset[0],name_list[0])

def print_friends(data, name):
    print "Number of Friends for " + name + ": " + str(len(data))
    for friend in data:
        print friend

if __name__ == '__main__':
    main()