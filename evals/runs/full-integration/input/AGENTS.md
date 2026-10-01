# Repository conventions

`src/cart.py` and `src/checkout.py` implement the same domestic shipping policy.
Amounts are nonnegative integer cents. Domain balance changes use Wallet's debit contract.
`src/registry.py` declares runtime event entry points; callbacks may have no direct call sites.
Review source read-only and preserve runtime contracts.
