# This entrypoint file to be used in development. Start by reading README.md
import medical_data_visualizer
from unittest import main
import matplotlib.pyplot as plt

# Test your function by calling it here
cat_plot = medical_data_visualizer.draw_cat_plot()
cat_plot.savefig('categorical_plot.png')

heat_map = medical_data_visualizer.draw_heat_map()
heat_map.savefig('heat_map.png')

plt.show()

# Run unit tests automatically
main(module='test_module', exit=False)