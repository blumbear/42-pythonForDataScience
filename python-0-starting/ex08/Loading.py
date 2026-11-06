def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progress bar every time a value is requested."""
    for i in lst:
        to_print = ''
        to_print += f"{((i * 100 // len(lst)) + 1):>3}%|"
        to_print += f"{'█' * ((i * 100 // len(lst)) + 1)}"
        to_print += f"{' ' * (100 - ((i * 100 // len(lst)) + 1))}| "
        to_print += f"{i + 1}/{len(lst)}"
        print(to_print, end="\r", flush=True)
        yield i
