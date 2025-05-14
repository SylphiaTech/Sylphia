import hashlib

def generate_wallet_hash(wallet):
    return hashlib.sha256(wallet.encode()).hexdigest()

def detect_sybil_wallets(wallets):
    seen_hashes = set()
    duplicates = []
    for w in wallets:
        h = generate_wallet_hash(w)
        if h in seen_hashes:
            duplicates.append(w)
        seen_hashes.add(h)
    return duplicates

def sybil_similarity_matrix(wallet_matrix):
    size = len(wallet_matrix)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = sum(1 for a, b in zip(wallet_matrix[i], wallet_matrix[j]) if a == b)
    return matrix