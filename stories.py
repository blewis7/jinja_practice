"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    'adventure',
    "Fairytale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    'emotion',
    "Urgency",
    ['verb', 'adjective', 'verb'],
    '''I really need to {verb}. I don't have much time left; this whole thing is making me very {adjective}. Please {verb} me, so I can finish in time.'''
)

story3 = Story(
    'vacation',
    "Beach Day",
    ['adjective', 'description', 'place', 'verb'],
    '''It is so {adjective} today! I love the beach, but this is not {description}! I would rather go to the {place} and {verb}.'''
)

stories = {s.code: s for s in [story1, story2, story3]}
