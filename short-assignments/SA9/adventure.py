from Vertex import Vertex

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()
    return vertex_name, adjacent, text


def load_story(filename):
    vertex_dict = {}
    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

            # YOU WRITE THIS PART
            # create a graph vertex here and add it to the dictionary
            vertex_dict[vertex_name] = Vertex(adjacent_vertices,text)

    file.close()
    return vertex_dict


def play_game():
    story_dict = load_story("story.txt")
    vertex = story_dict["START"]

    print("Welcome to the game. Type 'QUIT' at any time to stop.\n")

    while True:
        if vertex.adjacency_list == []:
            print(vertex)
            break

        user_input = input(str(vertex) + "\n")

        if user_input == "QUIT":
            break

        user_choice = ord(user_input) - 97
        next_vertex = vertex.adjacency_list[user_choice]
        vertex = story_dict[next_vertex]

play_game()