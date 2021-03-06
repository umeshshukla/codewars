"""Module to solve the code-kata https://www.codewars.com/kata/sudoku-solver."""

from math import sqrt, ceil
from itertools import islice
from operator import itemgetter
from collections import defaultdict

def sudoku_solver(m):
    """Return a valid Sudoku for a given matrix.
        Store all starting numbers by looping through the Sudoku square by square
        Find all missing numbers by subtracting the 2 sets
        Generate all starting spots and find the one with the least amount of digits missing
        Generate candidates by finding all possible numbers for a given starting point
        Pop the starting point from a sorted representation of the previously built list
        Update Sudoku if a fit is found
        Remove updated digit from all lists of missing number and as a possible candidates
        Repeat with next starting point
        If no immediate match is found, scrap candidated and rebuild until all digits have been
        inserted.
        """
    square_sides = int(sqrt(len(m)))
    rows_missing = defaultdict(list)
    rows_missing = initialize_d(rows_missing, square_sides)
    cols_missing = defaultdict(list)
    cols_missing = initialize_d(cols_missing, square_sides)
    squares_missing = defaultdict(list)
    squares_missing = {key:[] for key in range(1, square_sides ** 2 + 1)}
    squares_coords = {}
    dicts = rows_missing, cols_missing, squares_missing
    sq_nr = 0
    for row in range(0, square_sides ** 2, square_sides):
        for col in range(0, square_sides ** 2, square_sides):
            sq_nr += 1
            square = [islice(m[i], col, square_sides + col) for i in range(row, row + square_sides)]
            fill_given_numbers(square, row, col, sq_nr, dicts, squares_coords)
    for d in dicts:
        d = get_missing(d)
    m = fill_sudoku(m, dicts, squares_coords)
    return m


def initialize_d(d, square_sides):
    """Return an initialized dict so empty rows or columns in the Sudoku are
    correctly handled."""
    return {key:[] for key in range(square_sides ** 2)}


def fill_given_numbers(square, row, col, sq_nr, dicts, squares_coords):
    """Fill dicts with given numbers number for a given square."""
    rm, cm, sm = dicts
    for row_idx, sr in enumerate(square):
        for col_idx, sv in enumerate(sr):
            coord = (row + row_idx, col + col_idx)
            if sv == 0:
                squares_coords[coord] = sq_nr
                continue
            rm[coord[0]].append(sv)
            cm[coord[1]].append(sv)
            sm[sq_nr].append(sv)


def get_missing(d):
    """Return a dictionary with swapped values from given numbers to missing numbers."""
    for k, v in d.items():
        d[k] = set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(v)
    return d


def get_starting_spots(m, dicts, squares_coords):
    """Return a list with coordinates as starting point for sudoku solver."""
    rm, cm, sm = dicts
    starting_spots = []
    row = 0
    col = 0
    max = 20
    start = -1
    for col in range(9):
        for row in range(9):
            if m[row][col] == 0:
                square = squares_coords[(row, col)] - 1
                missing_numbers = len(cm[col]) + len(rm[row]) + len(sm[1 if square < 1 else square])
                starting_spots.append((row, col, missing_numbers))
    return starting_spots


def get_candidates(starting_spots, candidates, dicts, squares_coords):
    """Return a dict of candidates for all starting_spots in the Sudoko."""
    for coordinate in starting_spots:
        row, col, missing = coordinate
        rm, cm, sm = dicts
        candidates[(row, col)] = [n for n in cm[col] if n in rm[row] and n in sm[squares_coords[row, col]]]
    return candidates


def find_fit(candidates):
    """Return a tuple with coordinate and value to update from a sorted
    representation of a dict."""
    fit = sorted(candidates.items(), key=lambda x: len(x[1])).pop(0)
    row, col = fit[0]
    n = fit[1].pop()
    if len(fit[1]) == 0:
        return row, col, n
    return None

def update_sudoku(fit, m):
    """Return an updated Sudoku."""
    row, col, n = fit
    try:
        if m[row][col] != 0:
            raise ValueError
        m[row][col] = n
    except ValueError:
        raise ValueError('This coordinate has already been updated.')
    return m


def remove_updated_from_dicts(fit, dicts, squares_coords):
    """Return dicts with updated digit removed from missing digits."""
    row, col, n = fit
    rm, cm, sm = dicts
    rm[row].remove(n)
    cm[col].remove(n)
    sm[squares_coords[row, col]].remove(n)
    return dicts


def remove_from_candidates(fit, candidates):
    """Return candidates with updated digit removed from all coordinates."""
    row, col, n = fit
    del candidates[(row, col)]
    for k, v in candidates.items():
        if k[0] == row or k[1] == col:
            try:
                v.remove(n)
            except:
                continue
    return candidates


def fill_sudoku(m, dicts, squares_coords):
    """Return the solved Sudoku by continously updating numbers from the list of
    candidates. If no immediate candidates, rebuild the starting spots and list
    of candidates and repeat updating process until no more candidates."""
    candidates = {}
    starting_spots = get_starting_spots(m, dicts, squares_coords)
    starting_spots.sort(key=itemgetter(2))
    candidates =  get_candidates(starting_spots, candidates, dicts, squares_coords)
    if len(sorted(candidates.items(), key=lambda x: len(x[1])).pop(0)[1]) > 1: # no longer easily solvable
        return m
    while True:
        candidates_amt = len(candidates)
        try:
            fit = find_fit(candidates)
        except IndexError:
            return m
        if fit:
            m = update_sudoku(fit, m)
            dicts = remove_updated_from_dicts(fit, dicts, squares_coords)
            candidates = remove_from_candidates(fit, candidates)
            if not candidates:
                return m
        else:
            candidates = {} #we are no longer interested in current candidates
            starting_spots = []
            m = fill_sudoku(m, dicts, squares_coords)
