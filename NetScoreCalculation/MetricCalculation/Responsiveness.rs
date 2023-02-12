/*  Name:Matthew Nale
 *  Date of Last Edit: 2/12/2023
 *  
 *  Purpose: Calculate Responsiveness Metric of a given Github Repository
 *
 *  Details: Uses the Pull Request submetric and Size submetric to calculate the total Responsiveness weighting
*/

use std::env;

//calculate_pulls with determine the submetric weighting for Pull Requests, with a 50/50 split on frequency and recency
pub fn calculate_pulls(last_pull: f64, pull_frequency: f64) -> f64{
    //First calculates the recency scoring
    let mut recency: f64 = 0.0;
    if last_pull <= 7.0 {            //Less than 1 week
        recency = 1.0;
    }
    else if last_pull <= 14.0 {      //Less than 2 weeks
        recency = 0.9;
    }
    else if last_pull <= 30.0 {      //Less than 1 month
        recency = 0.8;
    }
    else if last_pull <= 60.0 {      //Less than 2 months
        recency = 0.7; 
    }
    else if last_pull <= 90.0 {      //Less than 3 months
        recency = 0.6;
    }
    else if last_pull <= 120.0 {     //Less than 4 months
        recency = 0.5;
    }
    else if last_pull <= 180.0 {     //Less than 6 months
        recency = 0.4;
    }
    else if last_pull <= 240.0 {     //Less than 8 months
        recency = 0.3;
    }
    else if last_pull <= 300.0 {     //Less than 10 months
        recency = 0.2;
    }
    else if last_pull <= 365.0 {     //Less than a year
        recency = 0.1;
    }
    else {
        recency = 0.0;               //Greater than a year
    }

    //Then calculates the pull frequency scoring
    let mut frequency : f64 = 0.0;

    if pull_frequency <= 7.0 {
        frequency = 1.0;
    }
    else if pull_frequency <= 14.0 {
        frequency = 0.9;
    }
    else if pull_frequency <= 21.0 {
        frequency = 0.8;
    }
    else if pull_frequency <= 30.0{
        frequency = 0.7;
    }
    else if pull_frequency <= 60.0 {
        frequency = 0.6;
    }
    else if pull_frequency <= 90.0 {
        frequency = 0.5;
    }
    else if pull_frequency <= 120.0{
        frequency = 0.4;
    }
    else if pull_frequency <= 150.0{
        frequency = 0.2;
    }
    else if pull_frequency <= 180.0 {
        frequency = 0.1;
    }
    else {
        frequency = 0.0;
    }

    return (0.5 * recency) + (0.5 * frequency);
}

pub fn calculate_size(repo_size: f64, num_contributors: f64) -> f64 {
    //Get how many files per contributor
    let mut unweighted : f64 = repo_size / num_contributors;
    
    if unweighted <= 0.5 {                   //0.5 files per cont
        return 1.0;
    }
    else if unweighted <= 1.0 {              //1 file per cont
        return 0.9;
    }
    else if unweighted <= 2.5 {              //2.5 files per cont
        return 0.8;
    }
    else if unweighted <= 5.0 {              //etc...
        return 0.7;
    }
    else if unweighted <= 10.0 {
        return 0.6;
    }
    else if unweighted <= 15.0 {
        return 0.5;
    }
    else if unweighted <= 20.0 {
        return 0.4;
    }
    else if unweighted <= 30.0 {
        return 0.3;
    }
    else if unweighted <= 40.0 {
        return 0.2;
    }
    else if unweighted <= 50.0 {
        return 0.1;
    }
    else {
        return 0.0;
    }
}

pub fn calculate_response(last_pull: f64, pull_frequency: f64, repo_size: f64, num_contributors: f64) ->f64 {
    let pull_weight : f64 = calculate_pulls(last_pull, pull_frequency);
    let size_weight : f64 = calculate_size(repo_size, num_contributors);

    let base_response : f64 = (pull_weight * 0.5) + (size_weight * 0.5);

    //Returns a 1-digit weighting value, rounded down if needed
    if base_response >= 1.0 {
        return 1.0;
    }
    else if base_response >= 0.9 {
        return 0.9;
    }
    else if base_response >= 0.8 {
        return 0.8;
    }
    else if base_response >= 0.7 {
        return 0.7;
    }
    else if base_response >= 0.6 {
        return 0.6;
    }
    else if base_response >= 0.5 {
        return 0.5;
    }
    else if base_response >= 0.4 {
        return 0.4;
    }
    else if base_response >= 0.3 {
        return 0.3;
    }
    else if base_response >= 0.2 {
        return 0.2;
    }
    else if base_response >= 0.1 {
        return 0.1;
    }
    else {
        return 0.0;
    }
}

fn main() {
    let args : Vec<String> = env::args().collect();                         //Collects the argv values into a vector called args
    let last_pull : f64 = args[1].parse().unwrap();                         //Converts the string values into a f64 value 
    let frequency : f64 = args[2].parse().unwrap();
    let repo_size : f64 = args[3].parse().unwrap();
    let num_contributors : f64 = args[4].parse().unwrap();

    let pull_weight = calculate_response(last_pull, frequency, repo_size, num_contributors);
    println!("README size weighting: {pull_weight}");
}