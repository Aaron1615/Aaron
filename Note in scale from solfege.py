def note(key,sol):
    """
    Takes a key (string) and a solfege location (string) as inputs, returns 
    the coresponding note in the scale
    """
    
    notes_sharp  =  ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    notes_flat   =  ['Ab','A','Bb','B','C','Db','D','Eb','E','F','Gb','G']
    tones = [0,2,4,5,7,9,11]
    sharp = ['C','G','D','A','E','B','F#']
    flat = ['F','Bb','Eb','Ab','Gb']
    solfege = ['Do','Re','Mi','Fa','So','La','Ti']
    s =True
    try:        
        fix = key[0].upper() + key[1:]
        sol = sol[0].upper() + sol[1]
        if fix in sharp:    
            start = notes_sharp.index(fix)

        elif fix in flat:
            start = notes_flat.index(fix)
            s = not s
    except IndexError:
        return("Please use proper Solfege notation")
    notes = []
    if s:
        try:
            changed = notes_sharp[start:len(notes_sharp)] + notes_sharp[0:start]
        except UnboundLocalError:
            return("Please use a proper key signature")
    else:
        changed = notes_flat[start:len(notes_flat)] + notes_flat[0:start]
    for i in tones:
        notes.append(changed[i])
    return(notes[solfege.index(sol)])
print(note("F","Re"))