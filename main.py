import numpy as np
# from pconst import const

test_data_1 = np.array([
   [[[ 0.33810245,  0.50561549, -2.08248016,  0.23325591,  0.53277484,
     1.97011148, -0.37944922, -1.34314863,  2.46978494,  1.11003021],
   [ 0.27297025, -0.32563047, -0.07173462,  0.46644386, -0.56924185,
    -0.99514498, -1.31138017, -0.65533014,  0.80680934, -2.07072258],
   [ 0.11522915,  0.49470898, -0.19826275,  2.38524529,  0.69625707,
     0.59525819,  0.01456653, -0.76295249,  0.22539998,  0.9780864 ],
   [-1.19762031, -0.12016672, -0.39350596, -0.65021846, -0.04573665,
    -0.50577363,  1.89160395, -2.72709064,  1.01974559,  0.94212133],
   [ 0.07368161,  0.14014638,  0.33364052,  0.92671546,  0.6037298,
     1.29983793,  0.48106357,  2.32106652,  1.69256248, -1.93717853],
   [ 0.67978298,  0.25327346, -2.66800411, -0.94412671, -0.26273395,
    -0.20955409, -0.75756119, -0.850852,    1.33903918, -2.36113146],
   [-0.14234271,  0.63042205,  0.70899265, -0.77700189, -0.5914539,
     1.00591701,  1.95847309, -0.70882734, -0.45067135,  0.94307293],
   [ 1.05134908, -1.07586943,  0.74146745, -0.90691587, -2.87408321,
    -2.37739167, -2.06621606, -2.53410406,  0.35270826,  0.07682136],
   [ 0.04071941,  0.22033619,  0.3929327, -0.71014051,  1.62909503,
     1.69380782, -1.28294949,  1.69189032,  1.08384622, -1.7884204 ],
   [ 1.17208356,  1.55891436, -0.49740564,  0.2131538,   0.10213847,
    -0.80960307, -0.01795926, -0.16208181, -0.26619135,  0.6435263 ]]]
 ])

test_kernel_1 = np.array(
[[[[ 0.17140324]],

  [[-0.27669533]],

   [[ 0.0273877]]],


 [[[ 0.31955287]],

  [[-0.39142543]],

  [[ 0.82467543]]],


 [[[-0.09708627]],

  [[-0.3703142]],

  [[-0.09663798]]]
 ])

test_bias = np.array([-0.11772539])

test_data_2 = np.array([
[[[ 0.33810245,  0.50561549, -2.08248016,  0.23325591,  0.53277484,
     1.97011148, -0.37944922, -1.34314863,  2.46978494,  1.11003021],
   [ 0.27297025, -0.32563047, -0.07173462,  0.46644386, -0.56924185,
    -0.99514498, -1.31138017, -0.65533014,  0.80680934, -2.07072258],
   [ 0.11522915,  0.49470898, -0.19826275,  2.38524529,  0.69625707,
     0.59525819,  0.01456653, -0.76295249,  0.22539998,  0.9780864 ],
   [-1.19762031, -0.12016672, -0.39350596, -0.65021846, -0.04573665,
    -0.50577363,  1.89160395, -2.72709064,  1.01974559,  0.94212133],
   [ 0.07368161,  0.14014638,  0.33364052,  0.92671546,  0.6037298,
     1.29983793,  0.48106357,  2.32106652,  1.69256248, -1.93717853],
   [ 0.67978298,  0.25327346, -2.66800411, -0.94412671, -0.26273395,
    -0.20955409, -0.75756119, -0.850852,    1.33903918, -2.36113146],
   [-0.14234271,  0.63042205,  0.70899265, -0.77700189, -0.5914539,
     1.00591701,  1.95847309, -0.70882734, -0.45067135,  0.94307293],
   [ 1.05134908, -1.07586943,  0.74146745, -0.90691587, -2.87408321,
    -2.37739167, -2.06621606, -2.53410406,  0.35270826,  0.07682136],
   [ 0.04071941,  0.22033619,  0.3929327, -0.71014051,  1.62909503,
     1.69380782, -1.28294949,  1.69189032,  1.08384622, -1.7884204 ],
   [ 1.17208356,  1.55891436, -0.49740564,  0.2131538,   0.10213847,
    -0.80960307, -0.01795926, -0.16208181, -0.26619135,  0.6435263 ]],

 [[0.33810245, 0.50561549, -2.08248016, 0.23325591, 0.53277484,
   1.97011148, -0.37944922, -1.34314863, 2.46978494, 1.11003021],
  [0.27297025, -0.32563047, -0.07173462, 0.46644386, -0.56924185,
   -0.99514498, -1.31138017, -0.65533014, 0.80680934, -2.07072258],
  [0.11522915, 0.49470898, -0.19826275, 2.38524529, 0.69625707,
   0.59525819, 0.01456653, -0.76295249, 0.22539998, 0.9780864],
  [-1.19762031, -0.12016672, -0.39350596, -0.65021846, -0.04573665,
   -0.50577363, 1.89160395, -2.72709064, 1.01974559, 0.94212133],
  [0.07368161, 0.14014638, 0.33364052, 0.92671546, 0.6037298,
   1.29983793, 0.48106357, 2.32106652, 1.69256248, -1.93717853],
  [0.67978298, 0.25327346, -2.66800411, -0.94412671, -0.26273395,
   -0.20955409, -0.75756119, -0.850852, 1.33903918, -2.36113146],
  [-0.14234271, 0.63042205, 0.70899265, -0.77700189, -0.5914539,
   1.00591701, 1.95847309, -0.70882734, -0.45067135, 0.94307293],
  [1.05134908, -1.07586943, 0.74146745, -0.90691587, -2.87408321,
   -2.37739167, -2.06621606, -2.53410406, 0.35270826, 0.07682136],
  [0.04071941, 0.22033619, 0.3929327, -0.71014051, 1.62909503,
   1.69380782, -1.28294949, 1.69189032, 1.08384622, -1.7884204],
  [1.17208356, 1.55891436, -0.49740564, 0.2131538, 0.10213847,
   -0.80960307, -0.01795926, -0.16208181, -0.26619135, 0.6435263]]
 ],

[[[ 0.33810245,  0.50561549, -2.08248016,  0.23325591,  0.53277484,
     1.97011148, -0.37944922, -1.34314863,  2.46978494,  1.11003021],
   [ 0.27297025, -0.32563047, -0.07173462,  0.46644386, -0.56924185,
    -0.99514498, -1.31138017, -0.65533014,  0.80680934, -2.07072258],
   [ 0.11522915,  0.49470898, -0.19826275,  2.38524529,  0.69625707,
     0.59525819,  0.01456653, -0.76295249,  0.22539998,  0.9780864 ],
   [-1.19762031, -0.12016672, -0.39350596, -0.65021846, -0.04573665,
    -0.50577363,  1.89160395, -2.72709064,  1.01974559,  0.94212133],
   [ 0.07368161,  0.14014638,  0.33364052,  0.92671546,  0.6037298,
     1.29983793,  0.48106357,  2.32106652,  1.69256248, -1.93717853],
   [ 0.67978298,  0.25327346, -2.66800411, -0.94412671, -0.26273395,
    -0.20955409, -0.75756119, -0.850852,    1.33903918, -2.36113146],
   [-0.14234271,  0.63042205,  0.70899265, -0.77700189, -0.5914539,
     1.00591701,  1.95847309, -0.70882734, -0.45067135,  0.94307293],
   [ 1.05134908, -1.07586943,  0.74146745, -0.90691587, -2.87408321,
    -2.37739167, -2.06621606, -2.53410406,  0.35270826,  0.07682136],
   [ 0.04071941,  0.22033619,  0.3929327, -0.71014051,  1.62909503,
     1.69380782, -1.28294949,  1.69189032,  1.08384622, -1.7884204 ],
   [ 1.17208356,  1.55891436, -0.49740564,  0.2131538,   0.10213847,
    -0.80960307, -0.01795926, -0.16208181, -0.26619135,  0.6435263 ]],
 [[0.33810245, 0.50561549, -2.08248016, 0.23325591, 0.53277484,
   1.97011148, -0.37944922, -1.34314863, 2.46978494, 1.11003021],
  [0.27297025, -0.32563047, -0.07173462, 0.46644386, -0.56924185,
   -0.99514498, -1.31138017, -0.65533014, 0.80680934, -2.07072258],
  [0.11522915, 0.49470898, -0.19826275, 2.38524529, 0.69625707,
   0.59525819, 0.01456653, -0.76295249, 0.22539998, 0.9780864],
  [-1.19762031, -0.12016672, -0.39350596, -0.65021846, -0.04573665,
   -0.50577363, 1.89160395, -2.72709064, 1.01974559, 0.94212133],
  [0.07368161, 0.14014638, 0.33364052, 0.92671546, 0.6037298,
   1.29983793, 0.48106357, 2.32106652, 1.69256248, -1.93717853],
  [0.67978298, 0.25327346, -2.66800411, -0.94412671, -0.26273395,
   -0.20955409, -0.75756119, -0.850852, 1.33903918, -2.36113146],
  [-0.14234271, 0.63042205, 0.70899265, -0.77700189, -0.5914539,
   1.00591701, 1.95847309, -0.70882734, -0.45067135, 0.94307293],
  [1.05134908, -1.07586943, 0.74146745, -0.90691587, -2.87408321,
   -2.37739167, -2.06621606, -2.53410406, 0.35270826, 0.07682136],
  [0.04071941, 0.22033619, 0.3929327, -0.71014051, 1.62909503,
   1.69380782, -1.28294949, 1.69189032, 1.08384622, -1.7884204],
  [1.17208356, 1.55891436, -0.49740564, 0.2131538, 0.10213847,
   -0.80960307, -0.01795926, -0.16208181, -0.26619135, 0.6435263]]
 ]
])

test_kernel_2 = np.array(
[[[[ 0.17140324, 0.17140324],
   [0.17140324, 0.17140324]],

  [[-0.27669533, -0.27669533],
   [-0.27669533, -0.27669533]],

   [[ 0.0273877, 0.0273877],
    [0.0273877, 0.0273877]]],


 [[[ 0.31955287, 0.31955287],
   [0.31955287, 0.31955287]],

  [[-0.39142543, -0.39142543],
   [-0.39142543, -0.39142543]],

  [[ 0.82467543, 0.82467543],
   [0.82467543, 0.82467543]]],


 [[[-0.09708627, -0.09708627],
   [-0.09708627, -0.09708627]],

  [[-0.3703142, -0.3703142],
   [-0.3703142, -0.3703142]],

  [[-0.09663798, -0.09663798],
   [-0.09663798, -0.09663798]]]
 ])

def Conv2D(input_data, kernel, bias, channels_in, channels_out, kernel_size=3, stride=1, padding=0):

    assert kernel.shape[-2] == input_data.shape[1]

    input_data = np.pad(input_data, ((0, 0), (0, 0), (padding, padding), (padding, padding)))
    shape = input_data.shape
    filters_applied = int((shape[-1] - kernel_size + stride) / stride)

    out = []
    for batch_id in range(shape[0]):
        batch = []

        for raw in range(0, shape[-2], 1):
            if raw + 3 > 12:
                break
            extracted = np.array([np.stack((input_data[batch_id, :, raw:raw + kernel_size, col:col + kernel_size]).reshape(1, -1), axis=1)
                                    for col in range(0, 12, 1)
                                    if col + kernel_size <= 12])
            extracted = np.array(extracted).reshape(filters_applied, kernel_size, kernel_size, 1, channels_in)
            result = extracted @ kernel

            # как упростить
            result = np.sum(result, axis=2)
            result = np.sum(result, axis=2)
            result = np.sum(result, axis=1) + bias
            batch.append(np.stack(result, axis=1).reshape(channels_out, filters_applied))

        batch = np.array(np.stack(batch, axis=1))
        out.append(batch)

    out = np.array(out)

test_1 = Conv2D(test_data_1, test_kernel_1, test_bias,  1, 1, 3, 1, 1)
test_1 = Conv2D(test_data_2, test_kernel_2, test_bias,  2, 2, 3, 1, 1)



