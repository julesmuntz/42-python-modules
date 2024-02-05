import os
import time


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    term_width = os.get_terminal_size().columns
    bar_width = term_width - 40
    start_time = time.time()
    for i in lst:
        i += 1
        elapsed_time = time.time() - start_time
        rate = (i - 1) / elapsed_time
        percentage = int((i / total) * 100)
        blocks = int((i / total) * bar_width)
        spaces = bar_width - blocks
        print(
            f"{str(percentage).rjust(3)}%|{'█' * blocks}{' ' * spaces}| {str(i).rjust(3)}/{total} [00:{str((int(elapsed_time))).zfill(2)}<00:00, {rate:.2f}it/s]",
            end="\r",
            flush=True,
        )
        yield i


def main():
    return


if __name__ == "__main__":
    main()
