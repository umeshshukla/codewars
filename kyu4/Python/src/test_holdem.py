"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-poker/python."""

import pytest

BOARDS = [
(['2', '3', '5', '6', '7'], True),
(['9','8','K','A','4'], False)
]

TEST_STRAIGHT = [
    (['2','2','3','3','4'],['5','6'], True),
    (['9','8','3','3','4'],['5','6'], False),
    (['9','8','K','Q','4'],['7','6'], False),
    (['2','6','3','7','A'],['5','4'], True),
    (['2', '3', '4', '5', '6'], ['K', 'Q'], True),
    (['8', 'J', 'Q', 'A', '2'], ['9', '10'], True),
]

TEST_INPUT = [
    (['6','3','3','5','2'],['3','3'],['4','7'], "A"),
    (['4','3','2','5','Q'],['7','8'],['5','7'], "B"),
    (['4','3','2','5','9'],['Q','A'],['A','Q'], "AB"),
    (['K', '3', '4', '5', '6'], ['7', '8'], ['7', '9'], "A"),
    (['2', '3', '4', '5', '6'], ['K', 'Q'], ['A', 'K'], "AB"),
    (['2', '3', '7', '8', 'Q'], ['3', '3'], ['7', '7'], "B"),
    (['8', 'J', 'Q', 'A', '2'], ['9', '10'], ['A', 'A'], "A"),
    (['2', '2', '3', '3', 'Q'], ['J', 'J'], ['Q', '3'], "B"),
]

@pytest.mark.parametrize('board, hole_cards, result', TEST_STRAIGHT)
def test_hand_is_straight(board, hole_cards, result):
    """Test that combination of board and hole_cards has a made hand value of straight."""
    from holdem import PokerHand
    heros_hand = PokerHand(board + hole_cards)
    assert heros_hand._is_straight == result

@pytest.mark.parametrize('board, hole_cards_hero, hole_cards_villain, result', TEST_INPUT)
def test_texasHoldem(board, hole_cards_hero, hole_cards_villain, result):
    """Test which hand is better given hero's hole cards and villain's hole cards."""
    from holdem import PokerHand, texasHoldem
    assert texasHoldem(board, hole_cards_hero, hole_cards_villain) == result
