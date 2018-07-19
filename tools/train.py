from optparse import OptionParser
from yolo.utils.process_config import process_config
import yolo  # This needs to be kept for backward compatibility

def run():
    parser = OptionParser()
    parser.add_option("-c", "--conf", dest="configure",
                      help="configure filename")
    (options, args) = parser.parse_args()
    if options.configure:
        conf_file = str(options.configure)
    else:
        print('Please specify --conf configure filename')
        return
    common_params, dataset_params, net_params, solver_params = \
        process_config(conf_file)

    dataset = eval(dataset_params['name'])(common_params, dataset_params)
    net = eval(net_params['name'])(common_params, net_params)
    solver = eval(solver_params['name'])(dataset, net, common_params,
                                         solver_params)
    solver.solve()


if __name__ == "__main__":
    run()
