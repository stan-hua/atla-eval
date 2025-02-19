import re


def _parse_output_absolute(output):
    # Start of non-capturing group
    # Match [RESULT] or [SCORE]
    # Match Score: or score:
    # Match Result: or [Result]:
    # HACK: Added **Result:** for Atla
    # Match "score of"
    # End of non-capturing group
    # Allow any whitespace
    # Allow opening brackets or whitespace
    # Capture the digit(s)
    # Start of non-capturing group
    # Allow closing brackets, whitespace, or end of string
    # Allow /5 with optional whitespace
    # or "out of 5" with flexible whitespace
    # End of non-capturing group
    # Match from the end of string 
    # HACK: Removed whitespace end anchor for Atla
    pattern = r"""
        (?:                         
            \[RESULT\]|\[SCORE\]|   
            Score:?|score:?|        
            \*\*Result:\*\*|        
            Result:?|\[Result\]:?|  
            score\s+of              
        )                           
        \s*                         
        (?:\(|\[|\s)*               
        (\d+)                       
        (?:                         
            (?:\)|\]|\s|$)|         
            (?:/\s*5|               
               \s*out\s*of\s*5)     
        )?                          
        (?:\s*)                    
    """
    match = re.search(pattern, output, re.IGNORECASE | re.VERBOSE)

    if match:
        result = int(match.group(1))
        if 1 <= result <= 5:  # Ensure the result is within the valid range
            feedback = output[: match.start()].strip()
            return output, result

    return None, None


def _parse_output_relative(output):
    explicit_pattern = r"""
        (?:                                # Start of non-capturing group
            \[RESULT\]|\[RESULT:\s*|        # Match [RESULT] or [RESULT:
            \[Response\s+|                  # Match [Response
            \*\*Result:\*\*|                # HACK: Match **Result:** for Atla
            \[Result\](?:\s+Response)?|     # Match [Result] or [Result] Response
            \[Result:\s*|                   # Match [Result:
            (?:^|\n)Result:?\s*             # Match Result: at the start of a line
        )                                   # End of non-capturing group
        \s*                                 # Allow any whitespace
        (A|B)                               # Capture A or B
        (?:\])?                             # Allow closing bracket, whitespace, or end of string
        (?:\s*)                            # Match from the end of string 
    """
    match = re.search(
        explicit_pattern, output, re.IGNORECASE | re.VERBOSE | re.MULTILINE
    )

    if match:
        result = match.group(1).upper()
        feedback = output[: match.start()].strip()
        return output, result

    return None, None


def parse_output(output, mode: str):
    assert mode in [
        "absolute",
        "relative",
    ], "Invalid mode. Supported modes are: 'absolute', 'relative'"

    if output is None:
        return None, None

    if mode == "absolute":
        return _parse_output_absolute(output)
    elif mode == "relative":
        return _parse_output_relative(output)
