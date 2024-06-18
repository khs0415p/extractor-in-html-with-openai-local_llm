import time
import tqdm
import argparse

from agent import Agent
from utils import extract_json, load_data
from file_writer import FileWriter

TEST_RANGE = (120, 130)


def main(args):

    data = load_data(args.task)

    writer = FileWriter(f"{args.type_llm}-{args.task}-{args.flow}-test.txt")
    agent = Agent(args.type_llm, args.task, args.flow)

    for i in tqdm.tqdm(range(TEST_RANGE[0], TEST_RANGE[1])):
        label = data[i]['ground_truth']
        start = time.time()
        answer = agent.run(data[i]['model_input'])
        elapsed_time = time.time() - start
        answer = extract_json(answer)
        writer.write(answer, label, i + 1, elapsed_time)


    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--type_llm', '-l', default='gpt', type=str, choices=['gpt', 'local'], help='type of llm')
    parser.add_argument('--task', '-t', default='html', type=str, choices=['html', 'css'], help='AI crawling tasks.')
    parser.add_argument('--flow', '-f', default='function_call', type=str, choices=['prompt', 'function_call'], help='method for json-generation.')
    args = parser.parse_args()
    main(args)