inputs = [1, 2, 3, 2.5]
weight1s = [0.2, 0.8, -0.5, 1]
weight2s = [0.5, -0.91, 0.26, -0.5]
weight3s = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0]*weight1s[0] + inputs[1]*weight1s[1] + inputs[2]*weight1s[2] + inputs[3]*weight1s[3] + bias1,
          inputs[0]*weight2s[0] + inputs[1]*weight2s[1] + inputs[2]*weight2s[2] + inputs[3]*weight2s[3] + bias2,
          inputs[0]*weight3s[0] + inputs[1]*weight3s[1] + inputs[2]*weight3s[2] + inputs[3]*weight3s[3] + bias3,
          ]
print(output)
