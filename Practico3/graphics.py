"""Generate scatter plots for the congruential generators."""

# pyright: reportMissingImports=false

import argparse
from typing import Callable, List

import matplotlib.pyplot as plt

from generators import generators as Generators


def build_sequence(
	seed: int,
	iterations: int,
	generator: Callable[..., int],
	*args,
) -> List[int]:
	"""Build a sequence starting from seed using the given generator."""
	values = [seed]
	current = seed

	for _ in range(iterations):
		current = generator(current, *args)
		values.append(current)

	return values


def plot_pairs(axis, values: List[int], title: str) -> None:
	"""Plot the pairs (x_i, x_i+1) for a generated sequence."""
	axis.scatter(values[:-1], values[1:], s=18)
	axis.set_title(title)
	axis.set_xlabel("x_i")
	axis.set_ylabel("x_i+1")
	axis.grid(True, alpha=0.25)


def main() -> None:
	parser = argparse.ArgumentParser(
		description=(
			"Generate and plot the pairwise points for the multiplicative, "
			"mixed and combined congruential generators."
		)
	)
	parser.add_argument("seed", type=int, help="Initial seed value")
	parser.add_argument("a", type=int, help="Multiplier")
	parser.add_argument("c", type=int, help="Increment")
	parser.add_argument("M", type=int, help="Modulus")
	parser.add_argument("iterations", type=int, help="Number of iterations")
	args = parser.parse_args()

	mul_values = build_sequence(
		args.seed, args.iterations, Generators.genMul, args.a, args.M
	)
	mix_values = build_sequence(
		args.seed, args.iterations, Generators.genMix, args.a, args.c, args.M
	)
	comb_values = build_sequence(
		args.seed, args.iterations, Generators.genComb_sum, args.a, args.c, args.M
	)

	_, axes = plt.subplots(1, 3, figsize=(15, 4.5), constrained_layout=True)
	plot_pairs(axes[0], mul_values, "GenMul: (x_i, x_i+1)")
	plot_pairs(axes[1], mix_values, "GenMix: (y_i, y_i+1)")
	plot_pairs(axes[2], comb_values, "GenComb: (z_i, z_i+1)")

	plt.show()


if __name__ == "__main__":
	main()
