## 01_01_memory_basics_stack_heap

To visualize this, imagine your RAM divided into two primary zones: the **Stack** (managed automatically, fast, LIFO structure) and the **Heap** (managed manually via `new`, slower, flexible size).

### Memory Diagram

| Memory Zone | Contents | Description |
| --- | --- | --- |
| **Stack** | `local_val` (10) | Local primitive variables. |
| **Stack** | `p1` (Address of `local_val`) | A pointer stored locally, pointing elsewhere on the stack. |
| **Stack** | `p2` (Address of `0xHeap...`) | The **pointer variable itself** is local. |
| **Heap** | `20` | The actual integer created by `new int(20)`. |

**The Visual Flow:**

1. `local_val` sits on the stack.
2. `p1` sits on the stack and has an arrow pointing to `local_val` (also on the stack).
3. `p2` sits on the stack, but its arrow crosses over into the **Heap** to point at the value `20`.

![01_01_memory_basics_stack_heap](Diagrams\01_01_memory_basics_stack_heap.png)

---

### Questions

**1. Does the variable p2 (the pointer itself) live on the Stack or the Heap?**
The variable `p2` lives on the **Stack**. In C++, any variable declared inside a function without the `static` keyword (like `int* p2`) is a local variable, and all local variables are allocated on the stack.

**2. Does the integer value 20 live on the Stack or the Heap?**
The integer value `20` lives on the **Heap**. This is because it was created using the `new` keyword. `new` tells the OS to find a spot in the heap large enough for an integer, initialize it to 20, and return that address.

**3. If p2 consumes 8 bytes of memory, where are those 8 bytes located?**
Those 8 bytes are located on the **Stack**. A pointer is just a variable that holds a memory address. While the *data* it points to is on the heap, the 8-byte address (the "house number") is stored in the `p2` slot on the stack.

---
---

