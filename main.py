#libs 
import ffmpeg
import click

formats = {".mp4", ".webm", ".avi", ".mov", ".wav", ".mp3", ".flac", ".ogg", ".mkv", ".flv"}

@click.command()
@click.option('-i','--inputf', required=True, help="input file.")
@click.option('-o','--output', required=True, help="output file.")


def main(inputf, output):
    print("Python Media Converter v0.1.")
    _, _, input_suffix = inputf.partition(".")
    _, _, output_suffix = output.partition(".")
    if "." + input_suffix in formats:
        print("Input file type OK.")
        if "." + output_suffix in formats:
            print("Output file type OK.")
            convert(inputf, output)
        else:
            print(f"Output file type error: {output_suffix}")
    else:
        print(f"Input file type error: {input_suffix}")


def convert(inp, out):
    try:
        ffmpeg.input(f"{inp}").output(f"{out}").run(overwrite_output=True, quiet=True)
    except Exception as e:
        print(f"Err: {e}")



if __name__ == "__main__":
    main()
