#functions which use pygame module

import pygame, settings as s, bfs

#drawing single rectangle
def draw_rect(COLOR, rects_list):
    for i in rects_list:
        pygame.draw.rect(s.win, COLOR, (i[0] + 1, i[1] + 1, s.rect_size - 1, s.rect_size - 1))


#drawing lines
def draw_lines():
    for i in range(0, s.edge, s.rect_size):
        pygame.draw.line(s.win, s.BLACK, (0, i), (s.edge, i))
        pygame.draw.line(s.win, s.BLACK, (i, 0), (i, s.edge))


#handling mouse buttons actions
def mouse_buttons(mouse_pos):
    if pygame.mouse.get_pressed()[0]:
        if s.rect_pos(mouse_pos) not in s.black_rects:
            s.black_rects.append(s.rect_pos(mouse_pos))
    if pygame.mouse.get_pressed()[2]:
        if s.rect_pos(mouse_pos) in s.black_rects:
            s.black_rects.remove(s.rect_pos(mouse_pos))
        s.graph = bfs.create_graph()


#drawing start and end of the shortest path
def draw_start_end():
    if s.start != (0, 1):
        pygame.draw.rect(s.win, s.RED, (s.start[0] + 1, s.start[1] + 1, s.rect_size - 1, s.rect_size - 1))
    if s.end != (0, 1):
        pygame.draw.rect(s.win, s.BLUE, (s.end[0] + 1, s.end[1] + 1, s.rect_size - 1, s.rect_size - 1))


#handling keyboard events
def events(mouse_pos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                s.s_path.clear()
                path = bfs.bfs_path()
                if path:
                    for i in path:
                        s.s_path.append((s.graph[1][i][1] * s.rect_size, s.graph[1][i][0] * s.rect_size))
                    s.s_path = s.s_path[1:-1]
                else:
                    print('No path')
            if event.key == pygame.K_w:
                s.s_path.clear()
            if event.key == pygame.K_1:
                s.start = s.rect_pos(mouse_pos)
            if event.key == pygame.K_2:
                s.end = s.rect_pos(mouse_pos)
            if event.key == pygame.K_s:
                draw_finding()

#drawing how to theshortest path is calculated
def draw_finding():
    for i in s.paths:
        tmp = []
        for j in i:
            tmp.append((s.graph[1][j][1] * s.rect_size, s.graph[1][j][0] * s.rect_size))

        draw_lines()

        draw_rect(s.BLACK, s.black_rects)
        draw_start_end()
        draw_rect(s.GREY, tmp[1:-1])
        pygame.display.update()
        #time.sleep(0.005)
        draw_rect(s.WHITE, tmp[1:-1])
        pygame.display.update()


#agragating all drawing functions
def draw():
    draw_lines()
    draw_rect(s.GREEN, s.s_path)
    draw_rect(s.BLACK, s.black_rects)
    draw_start_end()
