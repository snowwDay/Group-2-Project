// Team Screen
import React from 'react'
import { SafeAreaView, StyleSheet, } from 'react-native'

// Structured Screen Component Imports
import TeamHeader from '../components/teamScreen/TeamHeader'
import ScheduledTeam from '../components/teamScreen/ScheduledTeam'
import UnscheduledTeam from '../components/teamScreen/UnscheduledTeam'

// Screen
export default function TeamScreen({ navigation }) {
    return (
        <SafeAreaView style={ styles.container }>
            <TeamHeader />
            <ScheduledTeam />
            <UnscheduledTeam />
        </SafeAreaView>
    )
}

// Screen Style
const styles = StyleSheet.create({
    container: {
        backgroundColor: '#e4e7e4',
        flex: 1,
    },
})
