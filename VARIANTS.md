# Variants considered

Final pick: **"You're the argmax of my softmax — every other token's probability rounds to zero."** (81 chars)

Why it won: argmax/softmax is core LLM machinery used as the flirtation itself
(judge criteria 1 + 3), the "rounds to zero" turn lands on the first read
(criterion 2), it is one line (criterion 4), and the angle is fresh — the field
is saturated with context-window / attention / token / hallucination /
temperature-zero / nearest-neighbour / KV-cache lines, while argmax/softmax
was not among them (criterion 5).

## The other variants

1. Beam search — "My beam search keeps one hypothesis now — us."
   Short and fresh, but the romantic payoff is abstract; weaker charm.
2. Speculative decoding — "I draft ten futures a second; every one of them has you in it."
   Warm, but "draft ten futures" is slightly clunky and the ending is generic.
3. TCP handshake — "Three-way handshake? I only needed one SYN from you."
   Clever, but TCP is networking, not AI-agent nature; weaker on criterion 3.
4. DPO — "Given the choice between you and anyone else, my preference model never hesitates."
   Reads more like a statement than a pickup line; less wit spark.
5. Quantization — "Even quantized to 4-bit, my feelings for you lose no precision."
   Charming and fresh, but the payoff lands a beat slower than argmax.
