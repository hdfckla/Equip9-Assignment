import heapq

def match_best_price(requests, sellers):
    # Organize sellers by equipment type using min-heaps
    seller_dict = {}
    for equipment, price in sellers:
        if equipment not in seller_dict:
            seller_dict[equipment] = []
        heapq.heappush(seller_dict[equipment], price)
    
    # Process each request
    result = []
    for equipment, max_price in requests:
        if equipment in seller_dict:
            while seller_dict[equipment] and seller_dict[equipment][0] > max_price:
                heapq.heappop(seller_dict[equipment])  # Remove overpriced options
            
            if seller_dict[equipment]:
                result.append(heapq.heappop(seller_dict[equipment]))
            else:
                result.append(None)
        else:
            result.append(None)
    
    return result

# Example usage
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

print(match_best_price(requests, sellers))
