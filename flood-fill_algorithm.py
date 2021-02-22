def display(picture):
	result = ""
	for k in range(len(picture)):
		for c in range(len(picture[k])):
			result += f"{picture[k][c]} "
		print(result)
		result = ""

def correct_pixel(picture,pixel,old_color):
	return (0 <= pixel[0] < len(picture)) and (0 <= pixel[1] < len(picture[0])) and (picture[pixel[0]][pixel[1]] == old_color)

def flood_fill_algorithm(picture, starting_pixel, new_color):
	movements = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[-1,1],[1,1],[1,-1]]
	remains_to_be_done = [starting_pixel]
	old_color = picture[starting_pixel[0]][starting_pixel[1]]
	while len(remains_to_be_done) > 0:
		current_pixel = remains_to_be_done[0]
		del remains_to_be_done[0]
		picture[current_pixel[0]][current_pixel[1]] = new_color
		for movement in movements:
			neighbour_pixel = [current_pixel[0]+movement[0], current_pixel[1]+movement[1]]
			if correct_pixel(picture, neighbour_pixel, old_color):
				remains_to_be_done.append(neighbour_pixel)
	return picture

if __name__ == "__main__":
	my_picture = [["R", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
	              ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
	              ["R", "R", "R", "R", "B", "B", "B", "R", "R", "R"],
	              ["R", "B", "B", "B", "B", "B", "B", "R", "R", "R"],
	              ["R", "B", "B", "B", "B", "B", "B", "R", "R", "R"],
	              ["R", "B", "B", "B", "B", "B", "B", "R", "R", "R"],
	              ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
	              ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
	              ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
	              ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R"]]
	my_new_picture = flood_fill_algorithm(my_picture, [3,1], "V")
	display(my_new_picture)