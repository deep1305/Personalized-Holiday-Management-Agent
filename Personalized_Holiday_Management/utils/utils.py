from autogen_agentchat.conditions import TextMentionTermination

def get_termination_condition():
    """
    Get the termination condition for the holiday team agent
    """
    TERMINATION_WORD = "TERMINATE"
    text_mention_termination = TextMentionTermination(TERMINATION_WORD)
    return text_mention_termination