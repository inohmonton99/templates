import argparse
from nnicli import Experiment

def main(args):
    exp = Experiment()
    
    print(args.config)
    exp.start_experiment(args.config, port=args.port)
    
    status = exp.get_experiment_status()
    while status['status'] != 'DONE':
        status = exp.get_experiment_status()
    
    exp.stop_experiment()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=9000, help='NNI port')
    required_argument_group = parser.add_argument_group('required arguments')
    required_argument_group.add_argument('--config', help='NNI configuration', required=True)

    main(parser.parse_args())