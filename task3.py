good =  r"""
             www
        /n n\        /\
        |/^\|       /  \
        | , |       ^||^
         \_/         ||
         _U_         ||
       /`   `''-----'P3
      / |. .|''-----"||
      \'|   |        ||
       \|   |        ||
        E   |        ||
       /#####\       ||
       /#####\       ||
         |||         ||
         |||         ||
         |||         ||
         ||| gem     ||
        molom        Ll
    """
bad = r"""
                                        .
                                   / \
          I                       ( I )
         .I.                       .I.
        |   |    .I.       .I.    |   |
        |   |    | |       | |    |   |
        |   |    | |       | |    |   |
        |   |_.xx|_+-xxx---|_|xx._|   |
     _.-|   |   xx    xxx      xx |   |-._
   xX   '---'XX  _xx___xxx____ xx '---'XXX`,
  |    XXXXXX   '--XXXXX------'XXX      XX  |
   \ XXXXXX      XXXXX       XXXXX     XXX /
    `"XXX_     XXXXX       XXXXX     _XX-"'
          '"-XXXXX-------XXAoS-----"'
    """

drawbridge_raised = False
if not drawbridge_raised:
    outcome = ("Flicker: For the success ")
else:
    outcome = ("Doom: The other branch ")
print(outcome)