# Copyright 2016 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# Use this to run several variants of the tests.
ALL_VARIANT_FLAGS = {
  "default": [[]],
  "stress": [["--stress-opt", "--always-opt"]],
  "noturbofan": [["--no-turbo"]],
  "fullcode": [["--noopt", "--no-turbo"]],
  # No optimization means disable all optimizations. OptimizeFunctionOnNextCall
  # would not force optimization too. It turns into a Nop. Please see
  # https://chromium-review.googlesource.com/c/452620/ for more discussion.
  "nooptimization": [["--noopt"]],
  "asm_wasm": [["--validate-asm", "--stress-validate-asm", "--suppress-asm-messages"]],
  "wasm_traps": [["--wasm_guard_pages", "--wasm_trap_handler", "--invoke-weak-callbacks"]],
}

# FAST_VARIANTS implies no --always-opt.
FAST_VARIANT_FLAGS = {
  "default": [[]],
  "stress": [["--stress-opt"]],
  "noturbofan": [["--no-turbo"]],
  "fullcode": [["--noopt", "--no-turbo"]],
  # No optimization means disable all optimizations. OptimizeFunctionOnNextCall
  # would not force optimization too. It turns into a Nop. Please see
  # https://chromium-review.googlesource.com/c/452620/ for more discussion.
  "nooptimization": [["--noopt"]],
  "asm_wasm": [["--validate-asm", "--stress-validate-asm", "--suppress-asm-messages"]],
  "wasm_traps": [["--wasm_guard_pages", "--wasm_trap_handler", "--invoke-weak-callbacks"]],
}

ALL_VARIANTS = set(["default", "stress", "noturbofan", "fullcode",
                    "nooptimization", "asm_wasm", "wasm_traps"])
