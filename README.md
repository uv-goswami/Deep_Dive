### **Section 1: Memory Model**

---

#### **01. Memory Segments: The Stack vs. The Heap**

In systems programming (C++) and runtime environments (Python), understanding where data lives is the difference between a stable app and a `Segmentation Fault`.

| Feature | The Stack | The Heap |
| --- | --- | --- |
| **Primary Purpose** | Execution context (Local variables, function calls). | Dynamic, long-lived data. |
| **Allocation Speed** | **Ultra-fast.** Just moves the Stack Pointer () register. | **Slower.** Requires searching for free memory blocks. |
| **Management** | Automatic (LIFO - Last In, First Out). | Manual (C++) or Garbage Collected (Python). |
| **Scope** | **Thread-local.** Each thread gets its own. | **Global.** Shared by all threads (Race condition risk). |
| **Size** | Small/Limited (Fixed at startup). | Large/Flexible (Limited by RAM/VRAM). |

---

### **Deep Dive: The Mechanics**

#### **Physical Growth & Direction**

In a process's virtual address space, the **Stack** and **Heap** are designed to grow toward each other to maximize the use of available space:

* **The Stack:** Typically starts at a **high memory address** and grows **downward** (toward zero).
* **The Heap:** Starts at a **low memory address** (just above the Data segment) and grows **upward**.

#### **The "Performance Killer" Reality**

* **Spatial Locality:** The Stack is extremely cache-friendly because it uses contiguous memory. If you access a local variable, the next one is likely already in the CPU L1 cache.
* **Fragmentation:** The Heap suffers from **External Fragmentation**. Over time, as you `new` and `delete` objects of different sizes, the heap becomes a "Swiss cheese" of tiny holes, potentially causing allocation failures even if total free RAM is sufficient.

#### **Risk Assessment**

1. **Stack Overflow:** Triggered by deep recursion or massive local arrays (e.g., `int arr[1000000]`). The Stack Pointer moves past its allocated boundary.
2. **Memory Leaks:** Occur exclusively on the **Heap**. If the pointer to a heap-allocated block is lost before `delete` is called, that memory is "orphaned" until the process terminates.
3. **Concurrency:** Since the Heap is shared, two threads modifying the same Heap object without a `mutex` will cause data corruption.

---

