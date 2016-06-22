__author__ = 'johnfulgoni'

# import api_attempt
import create_dataset
import network_graph

jack_filename = 'Jacks_Facebook.csv'

def main():
    # api_attempt.start()

    name_list = []
    dataset = []

    jack_data = create_dataset.process_file(jack_filename)
    dataset.append(jack_data)
    name_list.append('Jack Holtgreive')

    G = network_graph.create_graph(dataset,name_list)

    print G.edges()

def print_friends(data):
    print "Number of Friends: " + str(len(data))
    for friend in data:
        print friend

if __name__ == '__main__':
    main()