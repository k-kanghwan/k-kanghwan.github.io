from md_head_num.MdHeadNum import MdHeadNum

target_path = ["_posts/Programming/Python/2025-06-01-Poetry-Usage.md"]


def main():
    # Create an instance of MdHeadNum
    md_head_num = MdHeadNum(target_path)
    md_head_num.numbering()
    md_head_num.save()


main()
