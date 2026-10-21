def recommend_books(prefs, books):
    """Rule engine: Matches books based on explicit logic rules."""
    scored_books = []

    for book in books:
        score = 0
        
        # Rule 1: Genre match is mandatory
        if book["genre"] == prefs["genre"]:
            score += 50
        else:
            continue

        # Rule 2: Pace match
        if book["pace"] == prefs["pace"]:
            score += 25

        # Rule 3: Length match
        if book["length"] == prefs["length"]:
            score += 25

        scored_books.append((score, book))

    # Sort books by highest match score descending
    scored_books.sort(key=lambda x: x[0], reverse=True)
    return scored_books 