import copy
def nextstep(state):
    state.append(copy.copy(state[-1]))
    state[0][0] = 0 if state[0][0] == 1 else 1
    for i in range(4):
        state[-1][i] = 0 if state[-1][i] == 1 else 1
        ret = 0
        for pri in range(len(state) - 1):
            if state[-1] == state[pri]:
                ret = 1
                break
        if ret == 1 or state[0][0] != state[-1][2] and (state[-1][1] == state[-1][2] or state[-1][2] == state[-1][3]):
            state[-1][i] = 0 if state[-1][i] == 1 else 1
            continue
        else:
            all_step.append(i)
            break
    if state[0][0] == 0 and state[-1][1:] == [0, 0, 0]:
        print(state)
    else:
        return nextstep(state)


if __name__ == '__main__':
    all_step = []
    initial_state = [[1], [1, 1, 1, 1]]
    nextstep(initial_state)
    step = ['啥没带', '带蔬菜', '带了羊', '带了狼']
    stp = 0
    for sp in all_step:
        stp += 1
        if stp % 2 == 1:
            print("第" + str(stp) + "步 " + "农夫从西岸到东岸" + step[sp] + "过去")
        else:
            print("第" + str(stp) + "步 " + "农夫从东岸到西岸" + step[sp] + "回来")