import { LineChart } from 'react-chartjs-2';

const chartData = {
    labels: ['Jan', 'Feb', 'Mar'],
    datasets: [
        {
            label: 'Job Metrics',
            data: [10, 20, 30],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }
    ]
};

export default function JobMetricsChart() {
    return (
        <LineChart data={chartData} />
    );
}
